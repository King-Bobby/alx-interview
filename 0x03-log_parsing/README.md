<h1>0x03. Log Parsing</h1>

0. Write a script that reads stdin line by line and computes metrics:

</li>Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size> (if the format is not this one, the line must be skipped)</li>
<li>After every 10 lines and/or a keyboard interruption (CTRL + C), print these statistics from the beginning<></li>
	Total file size: File size: <total size>		
	where <total size> is the sum of all previous <file size> (see input format above)
<li>Number of lines by status code:</li>
<li>possible status code: 200, 301, 400, 401, 403, 404, 405 and 500</li>
<li>if a status code doesn’t appear or is not an integer, don’t print anything for this status code</li>
	format: <status code>: <number>
<li><li><li> status codes should be printed in ascending order</li>
