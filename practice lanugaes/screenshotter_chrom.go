package main

import (
	"time"

	driver "/home/kali/Desktop/practice lanugaes/WebDriver/bin/main.go"
)

func main() {
	url := `https://google.com`
	driver.RunServer("./geckodriver")
	driver.GetSession()
	driver.Get(url)
	time.Sleep(8 * time.Second)
	driver.Screenshot("google")
	time.Sleep(8 * time.Second)

	defer driver.Kill()
}
