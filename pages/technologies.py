class technologies:
    def __init__(self, page):
        self.page=page
        self.tech=page.locator('(//a[@href="#"])[5]')

        self.eCom_devlop=page.locator('//strong[text()="eCommerce Development"]')
        self.eCom_d1=page.locator('(//a[@href="https://www.tranktechnologies.com/magento-development"])[1]')
        self.eCom_d2=page.locator('(//a[@href="https://www.tranktechnologies.com/opencart-development"])[1]')
        self.eCom_d3=page.locator('(//a[@href="https://www.tranktechnologies.com/codeigniter-development"])[1]')
        self.eCom_d4=page.locator('(//a[@href="https://www.tranktechnologies.com/wordpress-development"])[1]')
        self.eCom_d5=page.locator('(//a[@href="https://www.tranktechnologies.com/big-commerce"])[1]')
        self.eCom_d6=page.locator('(//a[@href="https://www.tranktechnologies.com/shopify-development"])[1]')
        self.eCom_d7=page.locator('(//a[@href="https://www.tranktechnologies.com/cs-cart-development"])[1]')
        self.eCom_d8=page.locator('(//a[@href="https://www.tranktechnologies.com/node-js-development"])[1]')
        self.eCom_d9=page.locator('(//a[@href="https://www.tranktechnologies.com/nopcommerce-design-and-development-company"])[1]')
        self.eCom_d10=page.locator('(//a[@href="https://www.tranktechnologies.com/woocommerce-development"])[1]')
        self.eCom_d11=page.locator('(//a[@href="https://www.tranktechnologies.com/laravel-development"])[1]')
        self.eCom_d12=page.locator('(//a[@href="https://www.tranktechnologies.com/prestashop-development"])[1]')
        self.eCom_d13=page.locator('(//a[@href="https://www.tranktechnologies.com/drupal-development"])[1]')
        self.eCom_d14=page.locator('(//a[@href="https://www.tranktechnologies.com/wix-development"])[1]')
        self.eCom_d15=page.locator('(//a[@href="https://www.tranktechnologies.com/joomla-development"])[1]')
        self.eCom_d16=page.locator('(//a[@href="https://www.tranktechnologies.com/react-js-development"])[1]')
        self.eCom_d17=page.locator('(//a[@href="https://www.tranktechnologies.com/express-js-development"])[1]')
        self.eCom_dev_list=[self.eCom_d1, self.eCom_d2, self.eCom_d3, self.eCom_d4, self.eCom_d5, 
                            self.eCom_d6, self.eCom_d7, self.eCom_d8, self.eCom_d9, self.eCom_d10, 
                            self.eCom_d11, self.eCom_d12, self.eCom_d13, self.eCom_d14, self.eCom_d15, 
                            self.eCom_d16, self.eCom_d17]


        self.mobile_app=page.locator('//strong[text()="Mobile App Development"]')
        self.mob_app1=page.locator('(//a[@href="https://www.tranktechnologies.com/react-native-mobile-app-development"])[1]')
        self.mob_app2=page.locator('(//a[@href="https://www.tranktechnologies.com/enterprise-mobile-app-development"])[1]')
        self.mob_app3=page.locator('(//a[@href="https://www.tranktechnologies.com/xamarin-mobile-app-development"])[1]')
        self.mob_app4=page.locator('(//a[@href="https://www.tranktechnologies.com/kotlin-mobile-app-development"])[1]')
        self.mob_app5=page.locator('(//a[@href="https://www.tranktechnologies.com/flutter-mobile-app-development"])[1]')
        self.mob_app6=page.locator('(//a[@href="https://www.tranktechnologies.com/ionic-mobile-app-development"])[1]')
        self.mob_app7=page.locator('(//a[@href="https://www.tranktechnologies.com/swift-mobile-app-development"])[1]')
        self.mob_app8=page.locator('(//a[@href="https://www.tranktechnologies.com/appointment-booking-development"])[1]')
        self.mob_app_list=[self.mob_app1, self.mob_app2, self.mob_app3, self.mob_app4, 
                           self.mob_app5, self.mob_app6, self.mob_app7, self.mob_app8]


        self.ai=page.locator('//strong[text()="Artificial Intelligence"]')
   

    def ecomDevClick(self):
        for i in self.eCom_dev_list:
            self.tech.click()
            self.eCom_devlop.hover()
            i.click()
            self.page.wait_for_load_state("load")
            self.page.go_back()

    def mobileAppClick(self):
        for i in self.mob_app_list:
            self.tech.click()
            self.mobile_app.hover()
            i.click()
            self.page.wait_for_load_state("load")
            self.page.go_back()

    def aiClick(self):
        self.tech.click()
        self.ai.hover()
        self.page.wait_for_load_state("load")
        self.page.go_back()     





