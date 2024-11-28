import ast

class PythonParser:
    def find_enclosing_context(self, file_content, line_start, line_end):
          tree = ast.parse(file_content)
          largest_context = None
          largest_size = 0

          for node in ast.walk(tree):
              if isinstance(node, (ast.FunctionDef, ast.ClassDef)):
                  start, end = getattr(node, 'lineno', None), getattr(node, 'end_lineno', None)
                  if start <= line_start and line_end <= end:
                      size = end - start
                      if size > largest_size:
                          largest_size = size
                          largest_context = node

          return largest_context
      
    def dry_run(self, file_content):
          ast.parse(file_content)
          return {'valid': True, 'error': ''}
