#include <stdio.h>
#include <strings.h>
#include <string.h>
#include <stdlib.h>
void usage() {
  static int slstack = {0};
  printf("This is a Help Usage.\n");
  exit(1);
}

int main(int argc, char *argv[]) {
  size_t length = strlen(argv[1]);
  printf("%d\n", length);
  return 0;
}

int main2(int argc, char *argv[]) {
  if (argc == 1) {
    printf("%s\n", argv[1]);
    usage();
  }
}
