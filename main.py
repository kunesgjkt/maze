from bludistatko1 import Bludiste
from vykresleni import BludisteCanvas
from robot import Robot
from robot_view import RobotView
import time


def pohybuj_robotem(robot, robot_view, kroky, vizualizace, prodleva=0.5):
    """Posouvá robota po naplánované cestě."""
    for krok in kroky:
        dx = krok[0] - robot.pozice[0]
        dy = krok[1] - robot.pozice[1]

        if robot.pohni_se((dx, dy)):
            robot_view.aktualizuj()
            vizualizace.okno.update()  # Aktualizuje GUI
            time.sleep(prodleva)  # Zpoždění mezi pohyby


if __name__ == "__main__":
    bludiste = Bludiste(4, 4, (0, 0), (3, 3), [
        [0, 1, 0, 0],
        [0, 1, 0, 1],
        [0, 0, 0, 1],
        [1, 1, 0, 'E']
    ])

    vizualizace = BludisteCanvas(bludiste)
    robot = Robot(bludiste)
    robot_view = RobotView(vizualizace, robot)

    # Vykreslení počátečního stavu
    vizualizace.vykresli_bludiste()
    robot_view.vykresli()

    # Vyhledání cesty a pohyb robota
    kroky = robot.hledej_cestu()
    pohybuj_robotem(robot, robot_view, kroky, vizualizace)

    vizualizace.okno.mainloop()
