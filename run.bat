
rem Edge browser
rem pytest -v -s TestCases/test_login.py --browser edge
rem pytest -v -s -n=2 TestCases/test_login.py --browser edge
rem pytest -v -s -m "sanity"--html=./Reports/Report1.html TestCases/ --browser edge
rem pytest -v -s -m "sanity and rgression"--html=./Reports/Report1.html TestCases/ --browser edge
rem pytest -v -s -m "regression" --html=./Reports/Report1.html TestCases/ --browser edge


rem Firefox Browser
rem pytest -v -s TestCases/test_login.py --browser fireforx
rem pytest -v -s -n=2 TestCases/test_login.py --browser fireforx
rem pytest -v -s -m "sanity"--html=./Reports/Report1.html TestCases/ --browser fireforx
rem pytest -v -s -m "sanity and rgression"--html=./Reports/Report1.html TestCases/ --browser fireforx
pytest -v -s -m "regression" --html=./Reports/Report_Firefox1.html TestCases/ --browser fireforx
