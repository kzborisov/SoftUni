function solve(inputData, criteria) {
    const [key, value] = criteria.split("-");

    JSON.parse(inputData)
        .filter((emp) => emp[key] === value || key == "all")
        .map((emp, idx) => {
            console.log(
                `${idx}. ${emp.first_name} ${emp.last_name} - ${emp.email}`
            );
        });
}

solve(
    `[{

    "id": "1",
    
    "first_name": "Ardine",
    
    "last_name": "Bassam",
    
    "email": "abassam0@cnn.com",
    
    "gender": "Female"
    
    }, {
    
    "id": "2",
    
    "first_name": "Kizzee",
    
    "last_name": "Jost",
    
    "email": "kjost1@forbes.com",
    
    "gender": "Female"
    
    },
    
    {
    
    "id": "3",
    
    "first_name": "Evanne",
    
    "last_name": "Maldin",
    
    "email": "emaldin2@hostgator.com",
    
    "gender": "Male"
    
    }]`,

    "gender-Female"
);
