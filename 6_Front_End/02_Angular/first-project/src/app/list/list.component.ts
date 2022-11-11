import { Component } from '@angular/core';

@Component({
  selector: 'app-list',
  templateUrl: './list.component.html',
  styleUrls: ['./list.component.css'],
})
export class ListComponent {
  myProp = 'Hello, World!';

  users = [
    { firstName: 'Ivan', lastName: 'Petrov' },
    { firstName: 'Kristian', lastName: 'Borisov' },
  ];

  constructor() {}
  showLastName = true;

  handleClickEvent = () => {
    this.showLastName = !this.showLastName;
  };
}
