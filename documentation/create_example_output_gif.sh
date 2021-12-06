asciinema rec -i 10 --overwrite -c 'python generate_example_output.py' output.cast
sed -i 's/\"height\": 9/\"height\": 24/g' output.cast
docker run --rm -v $PWD:/data asciinema/asciicast2gif -t asciinema -h 12 -w 80 output.cast output.gif
rm output.cast