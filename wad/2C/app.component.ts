// import { Component } from '@angular/core';
// import { EmailValidator } from '@angular/forms';
// import { RouterOutlet } from '@angular/router';

// @Component({
//   selector: 'app-root',
//   standalone: true,
//   imports: [RouterOutlet],
//   templateUrl: './app.component.html',
//   styleUrl: './app.component.css'
// })
export class AppComponent {
  title = 'Registration Form';

  displayName = ' ';
  displayAddress = ' ';
  displayContact = ' ';
  displayEmail = ' ';
  displayPassword = ' ';

  getValue(name:string, address:string, contact:string, email:string, password:string) {
    this.displayName = name;
    this.displayAddress = address;
    this.displayContact = contact;
    this.displayEmail = email;
    this.displayPassword = password;
  }
}