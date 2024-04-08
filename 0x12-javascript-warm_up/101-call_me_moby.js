#!/usr/bin/node
function executeTimes(x, func) {
  let i = 0;
  for(i = 0; i < x; i++) {
    func()
  }
}
