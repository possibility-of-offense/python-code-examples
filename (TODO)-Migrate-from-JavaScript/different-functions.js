// Content
// 1. Find nested values in object
// 2. Find value of nested property in object
// 3. Find most characters in a word
// 4. toFixed cloning

// LOGIC
// Find nested values in object
// Find nested values in object
// Find nested values in object

// const obj = {
//   value: 5,
//   node: {
//     value: 15,
//     node: {
//       value: 25,
//       node: {
//         value: 35,
//       },
//     },
//   },
// };

// function sum(node) {
//   if (!node.hasOwnProperty("node")) {
//     return node["value"];
//   } else {
//     return node["value"] + sum(node["node"]);
//   }
// }

// const res = sum(obj);
// // const res2 = sum(obj);

// console.log(res);
// // console.log(res2);

// LOGIC
// Find value of nested property in object
// Find value of nested property in object
// Find value of nested property in object

// const obj = {
//   name: "gosho",
//   sub: {
//     test: 1,
//     blah: {
//       amazing: "amazing",
//     },
//   },
// };

// function findInObj(o, k) {
//   const entries = Object.entries(o);

//   for (let i = 0; i < entries.length; i++) {
//     const [key, value] = entries[i];

//     if (key === k) {
//       return value;
//     }

//     if (typeof value === "object") {
//       const res = findInObj(value, k);

//       if (res !== null) {
//         return res;
//       }
//     }
//   }
//   return null;
// }

// const f = findInObj(obj, "amazing");
// console.log(f);

// LOGIC
// Find most characters in a word
// Find most characters in a word
// Find most characters in a word

// let str = "my 123 my da tka my 1234 what 123";

// function findMost(s) {
//   const obj = s.split(" ").reduce((acc, cur) => {
//     if (cur in acc) {
//       acc[cur] = acc[cur] + 1;
//     } else {
//       acc[cur] = 1;
//     }
//     return acc;
//   }, {});

//   const maxVal = Math.max(...Object.values(obj));

//   const entries = Object.entries(obj);
//   for (let i = 0; i < entries.length; i++) {
//     const [key, v] = entries[i];

//     if (v === maxVal) return key;
//   }
// }

// LOGIC
// toFixed cloning
// toFixed cloning
// toFixed cloning

// function toFixedClone(input, fraction) {
//   if (typeof input !== "number") {
//     throw new Error("The value should be of type number!");
//   }

//   const fractionDigits = Number(fraction);
//   if (isNaN(fractionDigits)) {
//     throw new Error(
//       "The fraction type should be number or string representation of a number!"
//     );
//   }

//   let out;
//   const floatingNumber = String(input).split(".").length > 1 ? true : false;

//   if (!floatingNumber) {
//     out = fractionDigits > 0 ? `${input}.${"0".repeat(fractionDigits)}` : input;
//   } else {
//     const lastDigits = String(input).split(".")[1].split("");
//     let sliced;

//     if (lastDigits.length > fractionDigits) {
//       sliced = lastDigits.slice(0, fractionDigits);
//       const leftOver = lastDigits.slice(fractionDigits);

//       if (Number(leftOver[0]) > 5) {
//         let popped = sliced.pop();
//         sliced = [...sliced, ++popped];
//       }

//       out = `${String(input).split(".")[0]}.${sliced.join("")}`;
//       return out;
//     }

//     out = `${String(input).split(".")[0]}.${lastDigits
//       .slice(0, fractionDigits)
//       .join("")}`;
//   }

//   return out;
// }

// const f = toFixedClone(5, "3");

// LOGIC
// Sorting array in descending order
// Sorting array in descending order
// Sorting array in descending order

// function sorting(a, b, c) {
//   const len = arguments.length;
//   let arr = [...arguments];

//   for (let i = 0; i < arr.length; i++) {
//     for (let k = i + 1; k < arr.length; k++) {
//       if (arr[k] > arr[i]) {
//         let temp = arr[i];

//         arr[i] = arr[k];
//         arr[k] = temp;
//       }
//     }
//   }

//   console.log(arr.join("\n"));
// }
// sorting(2, 5, 3);

function distance(x1, y1, x2, y2) {
  const xSqrt = x1 - x2;
  const ySqrt = y1 - y2;

  const d = xSqrt * xSqrt + ySqrt * ySqrt;

  console.log(Math.sqrt(d));
}
distance(2, 4, 5, 0);
