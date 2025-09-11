//getallen 1 per 1 van een array
const lijst = [4, 3, 9, 4, 7, 23, 67, 5, 1, 0]

for (let i = 0; i < lijst.length; i++) {
    console.log(lijst[i]);
}

//veelvouden van 4

for (let i = 1; i < 101; i++) {
    if (i % 4 == 0){
        console.log(i);
    }    
}

//10 tot 0

for (let i = 10; i >= 0; i--){
    console.log(i);
}