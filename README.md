# RouterOneKeyReboot
Reboot your routers with one key. 一键重启你的路由器
## Usage / 使用方法
Find the line that contains the password, replace default password like `admin` or `123456` with yours and save the file. (You should NOT leave your router's admin panel on the default password!)

For example, if your router admin password is `yourPassword123`, you should edit this:

`driver.find_element(By.ID, "pcPassword").send_keys("123456")`

To this:

`driver.find_element(By.ID, "pcPassword").send_keys("yourPassword123")`

Then install Python and the required packages, the command to install them should be at the top of the code. For example:

`# pip install selenium==4.9.0`

This case just run `pip install selenium==4.9.0` in your terminal.
## Contribution / 参与贡献
Wanna add code for your router model? We recommend using [Selenium IDE](https://www.selenium.dev/selenium-ide/). Just choose `Record a new test in a new project`, set a project name, type in your router's panel URL as the base URL then start recording. After rebooting manually once, stop recording and export your project as Python pytest. Remember to log out of your router panel first!

After test to making sure it works (we recommend to get rid of pytest), fork this repository and add your code, finally open a pull request. We'll review it as soon as possible.
