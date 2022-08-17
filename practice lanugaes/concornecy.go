package main

import (
	"fmt"
	"time"
)

func main() {
	go greeting("song")
	greeting("hello")
}

func greeting(s string) {
	for i := 0; i < 6; i++ {
		fmt.Println(s)
		time.Sleep(2 * time.Microsecond)
	}
}
