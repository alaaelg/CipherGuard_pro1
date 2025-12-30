import string
import secrets
import math

class SecurityEngine:
    @staticmethod
    def generate_password(length=16, use_upper=True, use_lower=True, use_digits=True, use_symbols=True):
        char_sets = []
        if use_upper: char_sets.append(string.ascii_uppercase)
        if use_lower: char_sets.append(string.ascii_lowercase)
        if use_digits: char_sets.append(string.digits)
        if use_symbols: char_sets.append("!@#$%^&*()-_=+[]{}|;:,.<>?")
        
        if not char_sets: return None, 0

        password = [secrets.choice(s) for s in char_sets]
        all_chars = ''.join(char_sets)
        remaining = length - len(password)
        password += [secrets.choice(all_chars) for _ in range(remaining)]
        
        secrets.SystemRandom().shuffle(password)
        final_pass = "".join(password)
        
        pool_size = len(all_chars)
        entropy = length * math.log2(pool_size)
        
        return final_pass, entropy

    @staticmethod
    def get_strength_meta(entropy):
        if entropy < 50: return "Weak", "red", 25
        if entropy < 80: return "Medium", "orange", 50
        if entropy < 120: return "Strong", "green", 80
        return "Excellent", "blue", 100