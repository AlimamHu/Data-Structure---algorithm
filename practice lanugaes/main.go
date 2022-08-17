package main

import (
	"fmt"
)

func main() {
	// array
	fmt.Println("Hello, World!")
	var first_array [5]string
	first_array[1] = "alimam"
	first_array[0] = "powerSong"
	first_array[2] = "mrROBOT"
	first_array[3] = "powerRANGER"
	first_array[4] = "MR_"

	fmt.Println(first_array)

	fmt.Println(first_array[2])

	fmt.Println(first_array[2:4], "length of array", len(first_array), "display array capicity:", cap(first_array))
	// veriable

}
