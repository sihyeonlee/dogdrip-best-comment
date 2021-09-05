from bs4 import BeautifulSoup
import requests
from PySide2.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from PySide2.QtCore import *
from ui_dogdrip import Ui_mainWindow
import sys
import webbrowser
from qt_material import apply_stylesheet


class Parse(QThread):
    update = Signal(list)
    status = Signal(bool)
    step = Signal(list)

    def __init__(self, parent=None):
        super().__init__()
        self.main = parent
        self.class_name = {'num': 'ed no text-xxsmall', 'title': 'ed title-link', 'link': 'ed link-reset',
                           'like': 'ed voteNum text-primary', 'comment_cnt': 'ed text-primary'}
        try:
            self.start_num = int(self.main.start_page)
            self.end_num = int(self.main.end_page)
            self.threshold = int(self.main.threshold_like)
        except:
            self.main.ui.label_status.setText("에러 발생")
            self.main.ui.button_search.setChecked(False)

    def parse_comment(self, content_id=None, comment_cnt=None):
        if content_id is None or comment_cnt is None:
            print("Error")
        else:
            comment_page_cnt = int(comment_cnt) // 50 + 1

            for comment_page in range(1, comment_page_cnt + 1):
                link = "https://www.dogdrip.net/index.php?document_srl=" + content_id + "&mid=dogdrip&cpage=" + str(comment_page)
                headers = {'User-Agent': 'Mozilla/5.0'}
                response = requests.get(link, timeout=5, headers=headers)
                content = BeautifulSoup(response.content, 'lxml')

                for raw_comment_id in content.find_all(True, {"class": ["ed comment-item clearfix", "ed comment-item clearfix depth"]}):
                    if self.main.flag is False:
                        self.status.emit(False)

                        return False

                    comment_id = str(raw_comment_id.attrs['id'])

                    comment = content.find("div", id=comment_id)
                    try:
                        real_comment_like = comment.find("span", "count").text
                    except:
                        continue

                    if int(real_comment_like) >= int(self.threshold):
                        class_name = comment_id + "_0 xe_content"

                        comment_text = comment.find("div", class_name)
                        real_comment_text = comment_text.find(['p', 'a']).text

                        if len(real_comment_text) == 0:
                            real_comment = "개드립콘"
                        else:
                            real_comment = real_comment_text

                        comment_link = "https://www.dogdrip.net/index.php?document_srl=" + str(content_id) + "&mid=dogdrip&cpage=" + str(comment_page) + "#" + comment_id

                        send_list = [real_comment, real_comment_like, comment_link]

                        self.update.emit(send_list)

    def parse_article_id(self):
        self.status.emit(True)

        for page_num in range(self.start_num, self.end_num + 1):
            link = "https://www.dogdrip.net/index.php?mid=dogdrip&page=" + str(page_num)
            headers = {'User-Agent': 'Mozilla/5.0'}
            response = requests.get(link, timeout=5, headers=headers)
            # print(response)
            raw_content = BeautifulSoup(response.content, 'lxml')

            raw_link = raw_content.find_all("a", self.class_name['link'])
            raw_comment_cnt = raw_content.find_all("span", self.class_name['comment_cnt'])

            content_list = []
            comment_cnt_list = []

            for test_link in raw_link:
                check = test_link['href']

                if check[0] != 'h':
                    pass
                else:
                    content_list.append(check)

            for comment_cnt in raw_comment_cnt:
                refine_comment_cnt = comment_cnt.text
                comment_cnt_list.append(refine_comment_cnt)

            for index, fusion in enumerate(zip(content_list, comment_cnt_list)):
                content_link = fusion[0]
                comment_cnt = fusion[1]
                content_id = content_link[24:]
                emit_list = [page_num, index + 1]
                self.step.emit(emit_list)
                if self.parse_comment(content_id, comment_cnt) is False:
                    return 0

    def run(self):
        self.parse_article_id()
        self.status.emit(False)


class Dogdrip(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)

        self.start_page = 0
        self.end_page = 0
        self.threshold_like = 0

    def update_status(self, status):
        if status is True:
            self.ui.label_status.setText("현재 상태 : 검색 중")
            self.ui.button_search.setText("검색 중지")
        else:
            self.ui.label_status.setText("현재 상태 : 검색 완료")
            self.ui.button_search.setText("검색")

    def update_step(self, step_list):
        text = str(step_list[0]) + "페이지 중 " + str(step_list[1]) + "번째 게시물"
        self.ui.label_step.setText(text)

    def openurl(self, item):
        # print(item.text())
        webbrowser.open(item.text())

    def update_comment_list(self, comment_list):
        # print(comment_list)
        current_cnt = self.ui.table_result.rowCount()
        self.ui.table_result.insertRow(current_cnt)

        for i in range(0, 3):
            item = QTableWidgetItem()
            if i == 1:
                item.setTextAlignment(Qt.AlignHCenter)
            self.ui.table_result.setItem(current_cnt, i, item)
            self.ui.table_result.item(current_cnt, i).setText(comment_list[i])

        self.ui.table_result.scrollToBottom()

    def search(self):
        # print(self.ui.button_search.isChecked())
        try:
            if int(self.ui.input_end_page.text()) - int(self.ui.input_start_page.text()) > 100:
                self.ui.label_status.setText("악용 방지를 위한 필터 작동")
                self.ui.button_search.setChecked(False)

                return False
            else:
                pass
        except:
            self.ui.label_status.setText("에러 발생")

        if self.ui.button_search.isChecked() is True:
            self.flag = True
            self.start_page = self.ui.input_start_page.text()
            self.end_page = self.ui.input_end_page.text()
            self.threshold_like = self.ui.input_like.text()

            self.th = Parse(self)
            self.th.update.connect(self.update_comment_list)
            self.th.status.connect(self.update_status)
            self.th.step.connect(self.update_step)

            self.th.start()
        else:
            self.flag = False
            self.th.quit()
            self.th.quit()

    def reset(self):
        current_row_cnt = self.ui.table_result.rowCount()

        for i in range(1, current_row_cnt + 1):
            self.ui.table_result.removeRow(current_row_cnt - i)


app = QApplication([])
apply_stylesheet(app, theme='dark_teal.xml')

dogdrip = Dogdrip()
dogdrip.show()

sys.exit(app.exec_())