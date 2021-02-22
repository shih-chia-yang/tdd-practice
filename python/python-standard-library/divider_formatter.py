#!/usr/bin/env python3

class formatter:
    @staticmethod
    def create_divider(title):
        length=80
        print(f'{title:-^{length}}')