function karaoke(input) {
  const participants = input[0].split(", ");
  const availableSongs = input[1].split(", ");

  const winningParticipans = {};

  participants.forEach((el) => {
    winningParticipans[el] = {
      awards: [],
    };
  });

  let index = 2;
  while (index < input.length) {
    if (input[index] === "dawn") {
      break;
    }

    let current = input[index].split(", ");
    let currentParticipant = current[0];
    let currentSong = current[1];
    let currentTitle = current[2];

    if (!winningParticipans.hasOwnProperty(currentParticipant)) {
      index++;
      continue;
    } else {
      if (availableSongs.includes(currentSong)) {
        if (
          !winningParticipans[currentParticipant].awards.includes(currentTitle)
        ) {
          winningParticipans[currentParticipant].awards.push(currentTitle);
        }
      }
    }

    index++;
  }

  let sorted = [];
  let noAwards = [];

  for (let key in winningParticipans) {
    winningParticipans[key].awards.sort();

    if (winningParticipans[key].awards.length) {
      noAwards.push(false);

      if (winningParticipans[key].awards.length) {
        sorted.push({ [key]: winningParticipans[key] });
      }

      sorted.sort((a, b) => {
        const k = Object.keys(a);
        const k1 = Object.keys(b);

        if (b[k1].awards.length === a[k].awards.length) {
          return k[0] - k1[0];
        } else {
          return b[k1].awards.length - a[k].awards.length;
        }
      });
    } else {
      noAwards.push(true);
    }
  }

  if (noAwards.every((el) => el === true)) {
    console.log("No awards");
    return;
  } else {
    sorted.forEach((el) => {
      const k = Object.keys(el);

      console.log(`${k[0]}: ${el[k[0]].awards.length} awards`);

      el[k[0]].awards.forEach((award) => {
        console.log(`--${award}`);
      });
    });
  }
}

karaoke(["Sino", "Vasko Naidenov - Nova Godina", "dawn"]);
karaoke([
  "Trifon, Vankata, Gesha",
  "Dragana - Kukavice, Bon Jovi - It's my life, Lorde - Royals",
  "Gesha, Bon Jovi - It's my life, Best Rock",
  "Vankata, Dragana - Kukavice, Best Srabsko",
  "Vankata, Dragana - Kukavice, Best Srabsko",
  "Vankata, Dragana - Kukavice, S Best Srabsko",
  "Vankata, PHP Web, Educational 101",
  "dawn",
]);
karaoke([
  "Gesha",
  "Bon Jovi - It's my life",
  "Gesha, Bon Jovi - It's my life, Best Rock",
  "Vankata, Dragana - Kukavice, Best Srabsko",
  "Vankata, Dragana - Kukavice, Stiga Tolko Srabsko",
  "Vankata, PHP Web, Educational 101",
  "dawn",
]);
