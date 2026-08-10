from config import BASE_URL


class blogmenus:
    def __init__(self, page):
        self.page=page
        self.blog=page.locator('(//a[@href="https://www.tranktechnologies.com/blog/"])[1]')

        self.app_dev=page.locator('(//a[@href="https://www.tranktechnologies.com/blog/category/app-development/"])[2]')
        self.artificial_int=page.locator('//a[@href="https://www.tranktechnologies.com/blog/category/artificial-intelligence/"]')
        self.content_marketing=page.locator('//a[@href="https://www.tranktechnologies.com/blog/category/content-marketing/"]')
        self.crm_dev=page.locator('//a[@href="https://www.tranktechnologies.com/blog/category/crm-development/"]')
        self.digital_market=page.locator('//a[@href="https://www.tranktechnologies.com/blog/category/digital-marketing/"]')
        self.ecom_dev=page.locator('(//a[@href="https://www.tranktechnologies.com/blog/category/ecommerce-development/"])[5]')
        self.email_marketing=page.locator('//a[@href="https://www.tranktechnologies.com/blog/category/email-marketing/"]')
        self.graphic_design=page.locator('(//a[@href="https://www.tranktechnologies.com/blog/category/graphic-design/"])[3]')
        self.software_it=page.locator('//a[@href="https://www.tranktechnologies.com/blog/category/software-it-company/"]')
        self.software_dev=page.locator('//a[@href="https://www.tranktechnologies.com/blog/category/software-development/"]')
        self.ui_ux=page.locator('(//a[@href="https://www.tranktechnologies.com/blog/category/ui-ux-design/"])[5]')
        self.web_dev=page.locator('(//a[@href="https://www.tranktechnologies.com/blog/category/web-development/"])[5]')


        self.blog_list=[self.app_dev, self.artificial_int, self.content_marketing, self.crm_dev, self.digital_market,
                        self.ecom_dev, self.email_marketing, self.graphic_design, self.software_it, self.software_dev,
                        self.ui_ux, self.web_dev]

    def blogMenuClick(self):
        for i in self.blog_list:
            self.blog.click()
            i.click()
            self.page.wait_for_load_state("load")
            self.page.goto(BASE_URL)
        