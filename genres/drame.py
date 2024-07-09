import pygame
import sys
import webbrowser

def show_drame_books(screen):
    font = pygame.font.Font(None, 36)
    books = ['Livre Drame 1', 'Livre Drame 2', 'Livre Drame 3']
    book_images = ['assets/livre_drame1.png', 'assets/livre_drame2.png', 'assets/livre_drame3.png']
    book_pdfs = ['assets/livre_drame1.pdf', 'assets/livre_drame2.pdf', 'assets/livre_drame3.pdf']
    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for idx, book in enumerate(books):
                    button = pygame.Rect(150, 100 + idx * 150, 500, 50)
                    if button.collidepoint(event.pos):
                        webbrowser.open(book_pdfs[idx])

        screen.fill((255, 255, 255))
        for idx, book in enumerate(books):
            button = pygame.Rect(150, 100 + idx * 150, 500, 50)
            pygame.draw.rect(screen, (0, 0, 0), button, 2)
            book_label = font.render(book, True, (0, 0, 0))
            screen.blit(book_label, (button.x + 10, button.y + 10))
            book_image = pygame.image.load(book_images[idx])
            book_image = pygame.transform.scale(book_image, (100, 150))
            screen.blit(book_image, (button.x + 400, button.y - 50))
        pygame.display.flip()

