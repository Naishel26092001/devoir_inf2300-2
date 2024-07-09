import pygame
import sys
import cv2
from genres.humour import show_humour_books
from genres.drame import show_drame_books
from genres.epouvante import show_epouvante_books
from genres.scifi import show_scifi_books
from video import play_background_video

def genre_menu(screen, background_video_path):
    font_large = pygame.font.Font(None, 48)
    genres = ['Humour', 'Drame', 'Épouvante', 'Sci-Fi']
    genre_images = ['assets/humour.png', 'assets/drame.png', 'assets/epouvante.png', 'assets/scifi.png']
    done = False

    cap, screen_width, screen_height = play_background_video(screen, background_video_path)

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                cap.release()
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for idx, genre in enumerate(genres):
                    button = pygame.Rect(150, 100 + idx * 100, 500, 50)
                    if button.collidepoint(event.pos):
                        if genre == 'Humour':
                            show_humour_books(screen)
                        elif genre == 'Drame':
                            show_drame_books(screen)
                        elif genre == 'Épouvante':
                            show_epouvante_books(screen)
                        elif genre == 'Sci-Fi':
                            show_scifi_books(screen)

        ret, frame = cap.read()
        if not ret:
            cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
            ret, frame = cap.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = cv2.transpose(frame)
        frame = cv2.flip(frame, 1)
        frame_surface = pygame.surfarray.make_surface(frame)
        screen.blit(pygame.transform.scale(frame_surface, (screen_width, screen_height)), (0, 0))

        for idx, genre in enumerate(genres):
            button = pygame.Rect(150, 100 + idx * 100, 500, 50)
            pygame.draw.rect(screen, (0, 0, 0), button, 2)
            genre_label = font_large.render(genre, True, (0, 0, 0))
            screen.blit(genre_label, (button.x + 10, button.y + 10))
            genre_image = pygame.image.load(genre_images[idx])
            genre_image = pygame.transform.scale(genre_image, (40, 40))
            screen.blit(genre_image, (button.x + 450, button.y + 5))
        pygame.display.flip()

    cap.release()
