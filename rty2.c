#include <stdio.h> 
#include <stdlib.h> 
#include <errno.h>
#include <unistd.h>

int main(int argc,char *argv[])


{
	int v = -1;
	char *feeds[] = {"https://lenta.ru/rss"};
	
	
	
	char *phrase = argv[1];
	int i;
	for (i = 0; i < 3 ; i++){
		char var [255];
		sprintf(var, "RSS_FEED=%s", feeds[i]);
		char *vars[] = {var, NULL};
		
		if ( execle ("/usr/bin/python3", "/usr/bin/python3",
			"script.py",phrase,NULL,vars) == -1) {
			
			fprintf (stderr, "не могу запустить скрипт: %d\n",
v);
			return 1;
			
			}
			
	}
	return 0;
}
