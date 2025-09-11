const getal = 3

for (let i = 1; i <= 3; i++) {
    if (getal > 5) {
        console.log("succes");
        break;
    }
    // else{
    //     console.log("3x geprobeert, mislukt");
    //     break;
    // }
    if (i === 3) {
        console.log("3x geprobeert, mislukt");
    }
}