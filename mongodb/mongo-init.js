db.createUser(
        {
            user: "tennis",
            pwd: "tennis",
            roles: [
                {
                    role: "readWrite",
                    db: "tennisdb"
                }
            ]
        }
);
