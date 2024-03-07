#include <uchar.h>
#include <locale.h>
#include <string.h>
#include <stdio.h>
#include <stdlib.h>

enum operations {
	DECODE,
	ENCODE,
};

int ustrlen(const char16_t * string) {
	int i = 0;
	while (*string++) {
		i++;
	}
	return i;
}

void ch_to_binary(char16_t ch, char * buf) {
	int i = 0;
	while (i < 16) {
		buf[15 - i] = ((ch >> i) & 1) ? 'e' : 'E';
		i++;
	}
	buf[16] = '\0';
}

char16_t binary_to_ch(const char * buf) {
	int i = 0;
	char16_t ch = 0;
	while (i < 16) {
		ch |= (buf[15 - i] == 'e') << i;
		i++;
	}
	return ch;
}

void rgb_prints(int red, int green, int blue, char * text) {
	printf("\033[38;2;%d;%d;%dm%s\033[38;2;255;255;255m", red, green, blue, text);
}

void rgb_printc(int red, int green, int blue, char16_t c) {
	printf("\033[38;2;%d;%d;%dm%lc\033[38;2;255;255;255m", red, green, blue, c);
}

void encode_dolphinscript(size_t length, const char * string) {
	char16_t buf[32];
	char binary[32];
	int j = 0;
	int wlength = 1;
	printf("\033[38;2;%d;%d;%dm", 196, 0, 255);
	while (wlength > 0) {
		int len, c;
		c = 0;
		len = ustrlen(buf);
		while (c < len) {
			ch_to_binary(buf[c], binary);
			printf("%s", binary);
			c++;
		}
		memset((char *) buf, 0, 64);
		wlength = mbrtoc16(buf, string + j, length, NULL);
		j += wlength;
	}
	printf("\033[38;2;255;255;255m");
}

void decode_dolphinscript(size_t length, const char * string) {
	int characters;
	if (length % 16) {
		rgb_prints(255, 0, 0, "invalid dolphinscript :c");
		return;
	}
	characters = length / 16;
	printf("\033[38;2;%d;%d;%dm", 196, 0, 255);
	for (int i = 0; i < characters; i++) {
		printf("%lc", binary_to_ch(string + (i * 16)));
	}
	printf("\033[38;2;255;255;255m");
}

void print_banner() {
	rgb_prints(0, 154, 255, "                                   __\nhttps://dolphinonkeys.com      _.-~  )\n                    _..--~~~~,'   ,-/     _\n                 .-' . . . .'   ,-','    ,' )\n               ,' . . . _   ,--~,-'__..-'  ,'\n             ,' . . .  (@)' ---~~~~      ,'\n            / . . . . '~~             ,-'\n           / . . . . .             ,-'\n          ;  . . . .  - .        ,'\n         :  . . . .       _     /\n        .  . . . .          \\`-.:\n       .  . . ./  - .          )\n      .   . . |  _____..---.._/ __ Seal :3 _\n~---~~~~----~~~~             ~~\n\n");
}

int main(int argc, char * argv[]) {
	char * flag;
	int op;
	int show_banner = 1;
	for (int i = 0; i < argc; i++) {
		if (strcmp(argv[i], "-n") == 0) {
			argv[i][0] = '\0';
			show_banner = 0;
		}
	}
	if (show_banner) {
		print_banner();
	}
	setlocale(LC_ALL, "");
	if (argc < 3) {
		rgb_prints(255, 0, 0, "not enough arguments :c\n");
		return -1;
	}
	flag = argv[1];
	if (flag[0] != '-' || (flag[1] != 'd' && flag[1] != 'e')) {
		rgb_prints(255, 0, 0, "invalid command :c\n");
		return -1;
	}
	op = flag[1] == 'e';
	for (int i = 2; i < argc; i++) {
		size_t length = strlen(argv[i]);
		const char * string = argv[i];
		if (length == 0) {
			continue;
		}
		if (op == ENCODE) {
			encode_dolphinscript(length, string);
		} else {
			decode_dolphinscript(length, string);
		}
	}
	printf("\n");
}
