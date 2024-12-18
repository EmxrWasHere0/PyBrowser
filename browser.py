from PyQt5.QtWidgets import QApplication, QMainWindow, QToolBar, QAction, QLineEdit
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QIcon
import sys
import os.path
dir_path = os.path.dirname(os.path.realpath(__file__).replace("\\","/"))
class Tarayici(QMainWindow):
    def __init__(self):
        super(Tarayici, self).__init__()
        self.setWindowTitle("PyBrowser")
        self.setGeometry(150, 150, 1280, 720)
        
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl(f"{dir_path}/main.html"))
        self.setCentralWidget(self.browser)
        self.setWindowIcon(QIcon(f"{dir_path}/PyBrowserLogo.ico"))
        
        toolbar = QToolBar()
        self.addToolBar(toolbar)
        
        geri = QAction("Back", self)
        geri.triggered.connect(self.browser.back)
        toolbar.addAction(geri)
        
        ileri = QAction("Forward", self)
        ileri.triggered.connect(self.browser.forward)
        toolbar.addAction(ileri)
        
        yenile = QAction("Refresh", self)
        yenile.triggered.connect(self.browser.reload)
        toolbar.addAction(yenile)
        
        anasayfa = QAction("Main Page", self)
        anasayfa.triggered.connect(self.go_home)
        toolbar.addAction(anasayfa)

        self.adresCubugu = QLineEdit()
        self.adresCubugu.returnPressed.connect(self.navigate_to_url)
        toolbar.addWidget(self.adresCubugu)
        
        self.browser.urlChanged.connect(self.update_url)

    def navigate_to_url(self):
        url = self.adresCubugu.text()
        if not url.startswith("http") or not url.startswith("https"):
            url = "http://google.com/search?q="+url
        self.browser.setUrl(QUrl(url))

    def update_url(self, q):
        self.adresCubugu.setText(q.toString())

    def go_home(self):
        self.browser.setUrl(QUrl(f"{dir_path}/main.html"))


app = QApplication(sys.argv)
pencere = Tarayici()
pencere.show()
sys.exit(app.exec_())