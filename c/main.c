#include <stdint.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <locale.h>
#include <unistd.h>
#include "main.h"

char * dolphin =
"                                   __\n"
"https://dolphinonkeys.com      _.-~  )\n"
"                    _..--~~~~,'   ,-/      _\n"
"                 .-' . . . .'   ,-','    ,' )\n"
"               ,' . . . _   ,--~,-'__..-'  ,'\n"
"             ,' . . .  (@)' ---~~~~      ,'\n"
"            / . . . . '~~             ,-'\n"
"           / . . . . .             ,-'\n"
"          ;  . . . .  - .        ,'\n"
"         :  . . . .       _     /\n"
"        .  . . . .          \\`-.:\n"
"       .  . . ./  - .          )\n"
"      .   . . |  _____..---.._/ __ Seal :3 __\n"
"~---~~~~----~~~~             ~~\n\n";

uint32_t current_colour = 0;
int no_colour = 0;
void set_colour(uint32_t colour) {
	if ((colour == current_colour) || no_colour) {
		return;
	}
	register uint8_t r, g, b;
	r = (colour >> 16) & 0xff, r;
	g = (colour >> 8) & 0xff, g;
	b = colour & 0xff, b;
	printf("\x1b[38;2;%d;%d;%dm", r, g, b);
	return;
}

void rgb_print(uint32_t colour, char * text) {
	set_colour(colour);
	printf("%s", text);
}

void rgb_putc(uint32_t colour, char chr) {
	set_colour(colour);
	printc(chr);
}

void uprint(uint16_t * str) {
	while (*str) {
		printf("%lc", *str);
		str++;
	}
}

void reset() {
	if (no_colour) {
		return;
	}
	fputs("\x1b[0m", stdout);
}

void parse_arguments(int argc, char * argv[], state_t * state) {
	int option = -1;
	state->string = NULL;
	state->op = NO_ARGS;
	state->silent = 0;
	while ((option = getopt(argc, argv, "hbne:d:")) != -1) {
		switch (option) {
			case 'd':
				state->string = optarg;
				state->op = DECODE;
				break;
			case 'e':
				state->string = optarg;
				state->op = ENCODE;
				break;
			case 'h':
				state->op = HELP;
			case 'b':
				state->silent = 1;
				break;
			case 'n':
				no_colour = 1;
			default:
				break;
		}
	}
}

uint8_t first_zero(uint8_t byte) {
	int i = 7;
	while ((byte >> i) & 1) {
		i--;
	}
	return 7 - i;
}

int utf8toutf16_strlen(char * string) {
	int size = strlen(string);
	int i = 0;
	int length = 0;
	while (i < size) {
		uint8_t chr = string[i];
		length++;
		if (!(chr & 0b10000000)) {
			i++;
			continue;
		}
		i += first_zero(chr);
	}
	return length;
}

void utf8toutf16(char * in, uint16_t * out) {
	int size = strlen(in);
	int i = 0;
	while (i < size) {
		uint8_t chr = in[i];
		if (!(chr & 0b10000000)) {
			*out++ = chr;
			i++;
			continue;
		}
		uint8_t length = first_zero(chr);
		uint16_t codepoint = 0;
		while ((length--) && (i < size)) {
			uint8_t chr = in[i] & 0x3f;
			codepoint <<= 6;
			codepoint |= chr;
			i++;
		}
		*out++ = codepoint;
	}
	*out = 0;
}

void encode(uint16_t word) {
	for (int i = 15; i >= 0; i--) {
		putchar(((word >> i) & 1) ? 'e' : 'E');
	}
}

uint16_t decode(char * string) {
	uint16_t word = 0;
	int i = 16;
	while (i--) {
		word <<= 1;
		word |= (*string++) == 'e';
	}
	return word;
}

int do_operation(char * string, int op) {
	set_colour(0xc400ff);
	switch (op) {
		case ENCODE: {
			int length = utf8toutf16_strlen(string);
			uint16_t * utf16 = malloc((length * 2) + 4);
			uint16_t * old = utf16;
			utf8toutf16(string, utf16);
			while (length--) {
				encode(*utf16++);
			}
			free(old);
			break;
		}
		case DECODE: {
			int length = strlen(string);
			uint16_t * utf16, * old;
			if (length & 0x0f) {
				rgb_print(0xff0000, "Please provide a valid operation\n");
				return -1;
			}
			length >>= 4;
			utf16 = malloc((length * 2) + 4);
			old = utf16;
			while (length--) {
				*utf16++ = decode(string);
				string += 16;
			}
			*utf16 = 0;
			uprint(old);
			free(old);
			break;
		}
	}
	putchar('\n');
	return 0;
}

int do_main(int argc, char * argv[]) {
	state_t state;
	parse_arguments(argc, argv, &state);
	if (!state.silent) {
		rgb_print(0x009aff, dolphin);
	}
	switch (state.op) {
		case HELP:
			set_colour(0x009aff);
			printf("usage: %s [options] [input]\n", argv[0]);
			printf("\n");
			printf("Options:\n");
			printf("  -e     encode to dolphin\n");
			printf("  -d     decode from dolphin\n");
			printf("  -b     hide banner\n");
			printf("  -h     display help\n");
			printf("  -n     no colour\n");
			return 0;
		case ENCODE:
		case DECODE:
			if (!state.string) {
				rgb_print(0xff0000, "ERROR\n");
				return -1;
			}
			return do_operation(state.string, state.op);
		case NO_ARGS:
			rgb_print(0xff0000, "Please provide a valid operation\n");
			return -1;
	}
	return -1;
}

int main(int argc, char * argv[]) {
	setlocale(LC_ALL, "en_US.UTF-8");
	do_main(argc, argv);
	reset();
}
