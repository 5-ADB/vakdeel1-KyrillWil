const temp = 69

switch (true) {
    case temp < 10:
        console.log("koud");
        break;
    case temp > 9 && temp < 11:
        console.log("nice");
        break;
    case temp > 19 && temp < 21:
        console.log("'t wotd warm");
        break;
    case temp > 30:
        console.log("zeer warm");
        break;
    default:
        break;
}