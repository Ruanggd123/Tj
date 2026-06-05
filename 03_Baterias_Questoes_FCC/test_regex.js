const text = "Considere o seguinte trecho em Python:\n\\\python\nx = 10\nprint(x)\n\\\\nSaída:";
const regex1 = /\\\(?:[a-zA-Z0-9]+)?\n([\s\S]*?)\n\\\/g;
const regex2 = /\\\[a-zA-Z0-9]*\r?\n([\s\S]*?)\r?\n\\\/g;
const text_win = text.replace(/\n/g, '\r\n');

console.log("Original match:", !!text.match(regex1));
console.log("Win match with regex1:", !!text_win.match(regex1));
console.log("Win match with regex2:", !!text_win.match(regex2));
