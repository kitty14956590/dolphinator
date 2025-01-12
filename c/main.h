typedef struct {
	char * string;
	int op;
	int silent;
} state_t;

enum {
	NO_ARGS,
	DECODE,
	ENCODE,
	HELP,
};

#define printc(c) putc(c, stdout)
