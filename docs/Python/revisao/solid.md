Acronimo, alguns principio que podem ajudar na organização e melhoria na construção
de projetos orientado a objeto.

S : Principio da Resposabilidade Unica (Single Responsability Principle)

O : Principio do Aberto e Fechado

L : Principio da Substiuição Liskove (Barbara Liskove)

I : Principio da Segregação de Interface

D : Principio da Inversão de Dependencia

# principio da responsabilidade unica Type Script

order.test.ts

```ts
import Item from "./Item";
import Order from "./Order";

test("Should calculate order sub total", function () {
  const order = new Order();
  order.addItem(new Item("Cigar", "Malboro", 10));
  order.addItem(new Item("Beer", "Itaipava", 5));
  order.addItem(new Item("Water", "Crystal", 2));
  const subtotal = order.getSubtotal();
  expect(subtotal).toBe(17);
});

test("Should calculate order taxes", function () {
  const order = new Order();
  order.addItem(new Item("Cigar", "Malboro", 10)); // 0.2 : 2
  order.addItem(new Item("Beer", "Itaipava", 5)); // 0.1 : 0.5
  order.addItem(new Item("Water", "Crystal", 2)); // 0 : 0
  const taxes = order.getTaxes();
  expect(taxes).toBe(2.5);
});

test("Should calculate order total", function () {
  const order = new Order();
  order.addItem(new Item("Cigar", "Malboro", 10));
  order.addItem(new Item("Beer", "Itaipava", 5));
  order.addItem(new Item("Water", "Crystal", 2));
  const total = order.getTotal();
  expect(total).toBe(19.5);
});
```

Item.ts

```ts
export default class Item {
  category: string;
  description: string;
  price: number;
  constructor(category: string, description: string, price: number) {
    this.category = category;
    this.description = description;
    this.price = price;
  }

  addItem(item: Item) {
    this.items.push(item);
  }

  getSubtotal() {
    let total = 0;
    for (const item of this.items) {
      total += item.price;
    }
    return total;
  }

  getTaxes() {
    let taxes = 0;
    for (const item of this.items) {
      if (item.category == "Cigar") {
        taxes += item.price * 0.2;
      }
      if (item.category == "Beer") {
        taxes += item.price * 0.1;
      }
    }
    return taxes;
  }

  get total() {
    return this.getSubtotal() + this.getTaxes();
  }
}
```

Order.ts

```ts
import Item from "./Item";
export default class Order {
  code: string;
  items: Item[];
  constructor() {
    this.code = `${Math.floor(Math.random() * 100000)}`;
    this.items = [];
  }
}
```
