export AUTH_CURL=$(curl --data-raw '{"username":"admin","password":"admin"}' --url 'http://localhost:5500/auth/login' -H 'Content-Type: application/json')
export AUTH_KEY=$(echo $AUTH_CURL | jq -r '.data')
#echo $AUTH_CURL
#echo $AUTH_KEY

echo "\nADMIN TEST"

#curl --data-raw '{"username": "admintest", "password": "admintest", "email": "admintest@financeadmin.com"}'  "localhost:5500/auth/register" -H "Content-Type: application/json"
curl "localhost:5500/account/transactions/2" -H "X-AUTH-KEY: $AUTH_KEY"
curl "localhost:5500/account/balance/2" -H "X-AUTH-KEY: $AUTH_KEY"
#curl --data-raw '{"user_id": 2, "amount": 5000}'  "localhost:5500/account/addbalance" -H "X-AUTH-KEY: $AUTH_KEY" -H "Content-Type: application/json"

echo "\nADMIN"

curl "localhost:5500/account/transactions/1" -H "X-AUTH-KEY: $AUTH_KEY"
curl "localhost:5500/account/balance/1" -H "X-AUTH-KEY: $AUTH_KEY"
curl --data-raw '{"user_id": 1, "destination_user_id": 2, "amount": 100000}'  "localhost:5500/account/addtransaction" -H "X-AUTH-KEY: $AUTH_KEY" -H "Content-Type: application/json"
