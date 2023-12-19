package main

import (
	"fmt"
	"io"
	"os"
)

func copyFile(source, destination string) error {
	sourceFile, err := os.Open(source)
	if err != nil {
		return err
	}
	defer sourceFile.Close()

	destFile, err := os.Create(destination)
	if err != nil {
		return err
	}
	defer destFile.Close()

	_, err = io.Copy(destFile, sourceFile)
	if err != nil {
		return err
	}

	fmt.Printf("File %s copied to %s\n", source, destination)
	return nil
}

func fileExists(filePath string) bool {
	_, err := os.Stat(filePath)
	return !os.IsNotExist(err)
}

func filesAreIdentical(file1, file2 string) (bool, error) {
	source, err := os.Open(file1)
	if err != nil {
		return false, err
	}
	defer source.Close()

	destination, err := os.Open(file2)
	if err != nil {
		return false, err
	}
	defer destination.Close()

	const chunkSize = 8192
	buffer1 := make([]byte, chunkSize)
	buffer2 := make([]byte, chunkSize)

	for {
		n1, err1 := source.Read(buffer1)
		n2, err2 := destination.Read(buffer2)

		if err1 != nil && err1 != io.EOF {
			return false, err1
		}

		if err2 != nil && err2 != io.EOF {
			return false, err2
		}

		if n1 != n2 || !equalBuffers(buffer1[:n1], buffer2[:n2]) {
			return false, nil
		}

		if err1 == io.EOF && err2 == io.EOF {
			break
		}
	}

	return true, nil
}

func equalBuffers(buf1, buf2 []byte) bool {
	if len(buf1) != len(buf2) {
		return false
	}
	for i := range buf1 {
		if buf1[i] != buf2[i] {
			return false
		}
	}
	return true
}

func main() {
	if len(os.Args) != 3 {
		fmt.Println("Usage: filecopy <source> <destination>")
		os.Exit(1)
	}

	source := os.Args[1]
	destination := os.Args[2]

	if fileExists(destination) {
		identical, err := filesAreIdentical(source, destination)
		if err != nil {
			fmt.Printf("Error comparing files: %v\n", err)
			os.Exit(1)
		}

		if identical {
			fmt.Printf("Files %s and %s are identical. Skipping copy.\n", source, destination)
			os.Exit(0)
		}
	}

	err := copyFile(source, destination)
	if err != nil {
		fmt.Printf("Error: %v\n", err)
		os.Exit(1)
	}
}
