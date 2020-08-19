package main

import (
	"fmt"
)

func main() {
	a := [][]int{{1, 2, 8, 9}, {2, 4, 9, 12}, {4, 7, 10, 13}, {6, 8, 11, 15}}
	b := 0
	rows := 4
	columns := 4
	fmt.Println(isNumberExist(a, rows, columns, b))
}

func isNumberExist(nums [][]int, rows int, columns int, n int) bool {
	if nums == nil || rows <= 0 || columns <= 0 {
		return false
	}
	row := 0
	column := columns - 1
	found := 0
	for {
		if row >= rows || column < 0 {
			break
		}
		found = nums[row][column]
		if found == n {
			return true
		}
		if found > n {
			column--
		} else {
			row++
		}
	}
	return false
}
