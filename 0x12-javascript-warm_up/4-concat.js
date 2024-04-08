#!/usr/bin/node
const arg1 = process.argv[2]
const arg2 = process.argv[3]
if (process.argv.length <= 3) {
  console.log('No argument')
} else {
  console.log(arg1 + ' is ' + arg2)
}
