from config import BASE_URL


class contactus:
    def __init__(self, page):
        self.page=page
        self.contactusLink=page.locator('(//a[@href="https://www.tranktechnologies.com/contact-us"])[1]')

        self.your_name=page.locator('(//input[@placeholder="Your Name"])[2]')
        self.your_mail=page.locator('(//input[@placeholder="Your Mail"])[2]')
        self.send_otp=page.locator('(//button[@type="button"])[2]')
        self.otp=page.locator('(//input[@placeholder="Enter OTP"])[2]')
        self.company_name=page.locator('(//input[@placeholder="Your Company"])[2]')
        self.service=page.locator('(//select[@name="service"])[2]')
        self.phone=page.locator('(//input[@name="phone"])[2]')
        self.message=page.locator('(//textarea[@placeholder="Message"])[2]')
        self.submit=page.locator('(//input[@type="submit"])[2]')

    def contactusfill(self):
        self.contactusLink.click()
        self.your_name.fill("Sowmiya")
        self.your_mail.fill("SS123@gmail.com")

        self.page.once("dialog", lambda dialog: dialog.accept())
        self.send_otp.click()
    
        # self.otp.fill(1234)
        self.company_name.fill("CG")
        self.service.select_option("Web Development")
        self.phone.fill("765312345")
        self.message.fill("Hello world!!")
        self.submit.click()
        # self.page.goto(BASE_URL)

        
        
