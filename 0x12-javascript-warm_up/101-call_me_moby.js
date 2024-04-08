#!/usr/bin/node
export function executeTimes (x, func) {     
  for (let i = 0; i < x; i++) {
    func();
  } 
}
