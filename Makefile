##
## EPITECH PROJECT, 2024
## Gomoku
## File description:
## Makefile
##

SRC	=	main.py

NAME	=	pbrain-gomoku-ai

TESTS    =	tests/

.PHONY: all clean fclean re tests_run

all: $(NAME)

$(NAME):
	cp $(SRC) $(NAME)
	chmod +x $(NAME)

clean:

fclean:
	rm -f $(NAME)

re: fclean all

tests_run:
