const eligibility = {
    or: [
        {
            // (age > 20 && age < 40) && nationality in ['UJA']
            and: [
                {
                    // 20 < age < 40
                    age: {
                        and: [
                            {
                                op: '>',
                                val: 20,
                            },
                            {
                                op: '<',
                                val: 40
                            }

                        ]
                    },
                    nationality: {
                        op: 'in',
                        val: ['UJA']
                    }
                }
            ]

        },
    ]
}

