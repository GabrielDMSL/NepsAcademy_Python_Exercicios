class Enemy:
    quantity_alive: int

    def __init__(self, id: int, x: int, y: int, alive: bool):
        self.id = id
        self.x = x
        self.y = y
        self.alive = alive

    def was_hit(self, x: int, y: int) -> None:
        if self.x == x and self.y == y and self.alive:
            self.alive = False
            Enemy.quantity_alive -= 1

if __name__ == "__main__":

    n = int(input())

    enemies = []
    Enemy.quantity_alive = n

    for id in range(n):
        x, y = map(int, input().split())
        enemies.append(Enemy(id, x, y, True))

    m = int(input())

    for i in range(m):
        x, y = map(int, input().split())

        for enemy in enemies:
            enemy.was_hit(x, y)

    print(f"vivos: {Enemy.quantity_alive}")
    print(f"mortos: {n - Enemy.quantity_alive}")

