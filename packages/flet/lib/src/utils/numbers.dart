double parseDouble(dynamic v, [double defValue = 0]) {
  if (v is double) {
    return v;
  } else if (v == null) {
    return defValue;
  } else {
    return double.tryParse(v.toString()) ?? defValue;
  }
}

double? parseDoubleFromJson(dynamic v, [double? defValue]) =>
    v != null ? parseDouble(v, defValue ?? 0) : defValue;

int parseInt(dynamic v, [int defValue = 0]) {
  if (v is int) {
    return v;
  } else if (v == null) {
    return defValue;
  } else {
    return int.tryParse(v.toString()) ?? defValue;
  }
}

int? parseIntFromJson(dynamic v, [int? defValue]) =>
    v != null ? parseInt(v, defValue ?? 0) : defValue;

bool parseBool(dynamic v, [bool defValue = false]) {
  if (v is bool) {
    return v;
  } else if (v == null) {
    return defValue;
  } else {
    return "true" == v.toString().toLowerCase();
  }
}

bool? parseBoolFromJson(dynamic v, [bool? defValue]) =>
    v != null ? parseBool(v, defValue ?? false) : defValue;
