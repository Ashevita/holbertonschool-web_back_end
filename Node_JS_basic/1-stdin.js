#!/usr/bin/env node

console.log('Welcome to Holberton School, what is your name?');

process.stdin.setEncoding('utf8');

process.stdin.on('data', (data) => {
  console.log(`Your name is: ${data.trim()}`);
});

process.stdin.on('end', () => {
  console.log('This important software is now closing');
});
