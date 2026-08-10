class vertical:
    def __init__(self, page):
        self.page=page
        self.ver=page.locator('(//a[@href="#"])[2]')

        self.trade=page.locator('//strong[text()="Trading"]')
        self.stock_tr1=page.locator('(//a[@href="https://www.tranktechnologies.com/stock-trading-mobile-app-development-company"])[1]')
        self.paper_tr2=page.locator('(//a[@href="https://www.tranktechnologies.com/paper-trading-app-development-company"])[1]')
        self.cfd_tr3=page.locator('(//a[@href="https://www.tranktechnologies.com/cfd-trading-app-development-company"])[1]')
        self.dev_tr4=page.locator('(//a[@href="https://www.tranktechnologies.com/stock-trading-development-in-massachusetts"])[1]')
        self.algo_tr5=page.locator('(//a[@href="https://www.tranktechnologies.com/algo-trading-app-development-company"])[1]')
        self.custom_tr6=page.locator('(//a[@href="https://www.tranktechnologies.com/custom-trading-software-development-company"])[1]')
        self.web_tr7=page.locator('(//a[@href="https://www.tranktechnologies.com/webportal-trading-development"])[1]')
        self.trade_list=[self.stock_tr1, self.paper_tr2, self.cfd_tr3, self.dev_tr4, self.algo_tr5, self.custom_tr6, self.web_tr7]


        self.retail_ecom=page.locator('//strong[text()="Retail and Ecommerce"]')
        self.re1=page.locator('(//a[@href="https://www.tranktechnologies.com/ecommerce-web-development-company"])[2]')
        self.re2=page.locator('(//a[@href="https://www.tranktechnologies.com/ecommerce-app-development"])[1]')
        self.retailEcom_list=[self.re1, self.re2]

        self.health_care=page.locator('//strong[text()="Healthcare"]')
        self.hc1=page.locator('(//a[@href="https://www.tranktechnologies.com/diet-and-nutrition-app-developement"])[1]')
        self.hc2=page.locator('(//a[@href="https://www.tranktechnologies.com/health-tracking-app"])[1]')
        self.healthcare_list=[self.hc1, self.hc2]


        self.fintech=page.locator('(//a[@href="https://www.tranktechnologies.com/fintech-mobile-app-development-company"])[1]')
        self.ft1=page.locator('(//a[@href="https://www.tranktechnologies.com/pos-software-development-company"])[1]')
        self.ft2=page.locator('(//a[@href="https://www.tranktechnologies.com/cryptocurrency-mobile-app-development-company"])[1]')
        self.fintech_list=[self.ft1, self.ft2]

        self.custom_app=page.locator('//strong[text()="Custom App"]')
        self.ca1=page.locator('(//a[@href="https://www.tranktechnologies.com/desktop-application-development-company"])[1]')
        self.ca2=page.locator('(//a[@href="https://www.tranktechnologies.com/custom-crm-development-company"])[1]')
        self.ca3=page.locator('(//a[@href="https://www.tranktechnologies.com/hrm-application-development-company"])[1]')
        self.ca4=page.locator('(//a[@href="https://www.tranktechnologies.com/erp-app-development-company"])[1]')
        self.ca5=page.locator('(//a[@href="https://www.tranktechnologies.com/travel-mobile-app-development-company"])[1]')
        self.ca6=page.locator('(//a[@href="https://www.tranktechnologies.com/e-learning-mobile-app-development-company"])[1]')
        self.ca7=page.locator('(//a[@href="https://www.tranktechnologies.com/dating-app-development-company"])[1]')
        self.ca8=page.locator('(//a[@href="https://www.tranktechnologies.com/real-estate-mobile-app-development-company"])[1]')
        self.ca9=page.locator('(//a[@href="https://www.tranktechnologies.com/usa/custom-crm-development-company-usa"])[1]')
        self.custom_list=[self.ca1, self.ca2, self.ca3, self.ca4, self.ca5, self.ca6, self.ca7, self.ca8, self.ca9]

        
    def tradingclick(self):
        for i in self.trade_list:
            self.ver.click()
            self.trade.hover()
            i.click()
            self.page.wait_for_load_state("load")
            self.page.go_back()

    def retailEcomClick(self):
        for i in self.retailEcom_list:
            self.ver.click()
            self.retail_ecom.hover()
            i.click()
            self.page.wait_for_load_state("load")
            self.page.go_back()

    def healthCareClick(self):
        for i in self.healthcare_list:
            self.ver.click()
            self.health_care.hover()
            i.click()
            self.page.wait_for_load_state("load")
            self.page.go_back()

    def fintechClick(self):
        for i in self.fintech_list:
            self.ver.click()
            self.fintech.hover()
            i.click()
            self.page.wait_for_load_state("load")
            self.page.go_back()

    def customAppClick(self):
        for i in self.custom_list:
            self.ver.click()
            self.custom_app.hover()
            i.click()
            self.page.wait_for_load_state("load")
            self.page.go_back()

    

    