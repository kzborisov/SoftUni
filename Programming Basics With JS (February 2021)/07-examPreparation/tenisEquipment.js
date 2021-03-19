// Task 1 - Tenis Equipment

function tenisEquipment(input){
    // Read Input
    let rocketPrice = Number(input.shift());
    let rocketsCount = Number(input.shift());
    let sneakersCount = Number(input.shift());

    // Logic
    let totalRocketsPrice = rocketsCount * rocketPrice;
    let sneakersPrice = sneakersCount * (rocketPrice / 6);
    let otherEquipment = (totalRocketsPrice + sneakersPrice) * 0.2;

    let totalPrice = totalRocketsPrice + sneakersPrice + otherEquipment;

    let djokovicPrice = totalPrice / 8;
    let sponsorsPrice = totalPrice * (7/8);

    // Print Result
    console.log(`Price to be paid by Djokovic ${Math.floor(djokovicPrice)}`);
    console.log(`Price to be paid by sponsors ${Math.ceil(sponsorsPrice)}`);
}

tenisEquipment(["850",
"4",
"2"]);