echo "# subprocess_example" >> README.md
git init
git add README.md
git add .
git commit -m "first commit"
git branch -M main
git remote add origin git@github.com:cklam12345/subprocess_example.git
git push -u origin main
