function secretSanta(inputs) {
  const numToSubtract = Number(inputs[0]);
  let index = 1;
  let names = [];

  while (index < inputs.length) {
    if (inputs[index] === "end") {
      break;
    }
    let nameElement = "";

    for (let i = 0; i < inputs[index].length; i++) {
      let charCode = inputs[index][i].charCodeAt(0);
      charCode = charCode - numToSubtract;
      nameElement += String.fromCharCode(charCode);
    }

    console.log(nameElement);

    let breaking = false;
    let name = "";

    if (nameElement.includes("@")) {
      const ind = nameElement.indexOf("@");

      for (let k = ind + 1; k < nameElement.length; k++) {
        if (nameElement[k] === "-" || nameElement[k] === "@") {
          breaking = true;
          break;
        }

        name += nameElement[k];
      }
    }

    let toAppend = "";
    if (!breaking && nameElement.includes("!G!")) {
      for (let k = 0; k < name.length; k++) {
        const test = name[k].match(/[a-zA-Z]/gi);

        if (test !== null) {
          toAppend += name[k];
        } else {
          break;
        }
      }

      names.push(toAppend);
    }

    index++;
  }

  if (names.length) {
    names.forEach((el) => console.log(el));
  }
}

secretSanta([
  4,
  "~lwzjkl~jenlymfDFsffmiCwozwlzjln%K%",
  "0zfjrl}xnrlDWeqqmi/wnznlwzjnn%K%onhfhnf",
  ";:<lyiljz{onzDPere=;=9<;8=rhknlf%K%",
  "Wonvfkmwzkmpwvzkm'lhjnlDWeqerxle0wlnzj{nz%K%nohwn",
  "DReh}e=<4lhzj1%K%",
  "end",
]);

// secretSanta([
//   3,
//   "N}eideidmk$'(mnyenmCNlpamnin$J$",
//   "ddddkkkkmvkvmCFrqqru-nvevek$J$nmgievnge",
//   "ppqmkkkmnolmnnCEhq/vkievk$Q$",
//   "yyegiivoguCYdohqwlqh/kguimhk$J$",
//   "end",
// ]);

// secretSanta([
//   3,
//   "CNdwhamigyenumje$J$",
//   "CEreelh-nmguuejn$J$",
//   "CVwdq&gnmjkvng$Q$",
//   "end",
// ]);
