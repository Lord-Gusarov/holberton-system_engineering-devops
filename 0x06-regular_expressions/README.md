##Intructions
For this project, you have to build your regular expression using Oniguruma,
a regular expression library that which is used by Ruby by default. Note that
other regular expression libraries sometimes have different properties.

Because the focus of this exercise is to play with regular expressions (regex),
here is the Ruby code that you should use, just replace the regexp part,
meaning the code in between the //:

```
sylvain@ubuntu$ cat example.rb
#!/usr/bin/env ruby
puts ARGV[0].scan(/127.0.0.[0-9]/).join
sylvain@ubuntu$
sylvain@ubuntu$ ./example.rb 127.0.0.2
127.0.0.2
sylvain@ubuntu$ ./example.rb 127.0.0.1
127.0.0.1
sylvain@ubuntu$ ./example.rb 127.0.0.a
```

# Tasks

### 0. Simply matching Holberton
* The regular expression must match Holberton
* Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method
* 		file:: 0-simply_match_holberton.rb

### 1. Repetition Token #0
![alt text](https://holbertonintranet.s3.amazonaws.com/uploads/medias/2020/9/e7db3c377d46453588fc84f3a975661d142fee91.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUWMNL5ANN%2F20210222%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20210222T172044Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=d5e39816807d8ef756470066dd509ff007856abf37ca8b5dd626a00bed8269fb)
* Find the regular expression that will match the above cases
* Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method
* 		file:: 1-repetition_token_0.rb

### 2. Repetition Token #1
![alt text](https://holbertonintranet.s3.amazonaws.com/uploads/medias/2020/9/c59ff11db195d5cf17d1790a5141ae2f234786d2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUWMNL5ANN%2F20210222%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20210222T172044Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=161393b26eb86c58375e241f6ac321a016c2e595d6086e48d9ec3b27085a89b5)
* Find the regular expression that will match the above cases
* Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method
* 		file:: 2-repetition_token_1.rb

