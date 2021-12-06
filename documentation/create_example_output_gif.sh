cp type_promot.cast output.cast
asciinema rec -i 10 --append -c 'python generate_example_output.py' output.cast
sed -i 's/\"height\": ./\"height\": 24/g' output.cast
docker run --rm -v $PWD:/data asciinema/asciicast2gif -t asciinema -h 13 -w 80 output.cast output.gif
rm output.cast