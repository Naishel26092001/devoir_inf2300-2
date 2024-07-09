import pygame
import sys
import webbrowser
import numpy as np

def generate_fractal(t, width, height):
    surface = pygame.Surface((width, height))
    for x in range(width):
        for y in range(height):
            c = complex(-2 + x * 4.0 / width, -2 + y * 4.0 / height)
            z = complex(0, 0)
            iterations = 0
            max_iterations = 100
            while abs(z) <= 2 and iterations < max_iterations:
                z = z * z + c
                iterations += 1
            color = (iterations % 8 * 32, iterations % 16 * 16, iterations % 32 * 8)
            surface.set_at((x, y), color)
    return surface

def show_scifi_books(screen):
    font = pygame.font.Font(None, 36)
    books = ['Livre Sci-Fi 1', 'Livre Sci-Fi 2', 'Livre Sci-Fi 3']
    book_images = ['assets/livre_scifi1.png', 'assets/livre_scifi2.png', 'assets/livre_scifi3.png']
    book_pdfs = ['assets/livre_scifi1.pdf', 'assets/livre_scifi2.pdf', 'assets/livre_scifi3.pdf']
    done = False
    t = 0

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

        fractal_surface = generate_fractal(t, screen.get_width(), screen.get_height())
        screen.blit(fractal_surface, (0, 0))
        t += 1

        for idx, book in enumerate(books):
            button = pygame.Rect(150, 100 + idx * 150, 500, 50)
            pygame.draw.rect(screen, (0, 0, 0), button, 2)
            book_label = font.render(book, True, (0, 0, 0))
            screen.blit(book_label, (button.x + 10, button.y + 10))
            book_image = pygame.image.load(book_images[idx])
            book_image = pygame.transform.scale(book_image, (100, 150))
            screen.blit(book_image, (button.x + 400, button.y - 50))
        pygame.display.flip()

