#!/usr/bin/env ruby

require "pathname"

root = Pathname.new(__dir__).parent
missing = []

(root.glob("*.html") + root.glob("projects/*.html")).each do |file|
  file.read.scan(/(?:src|href|poster)=["']([^"']+)["']/).flatten.each do |reference|
    next if reference.match?(%r{^(?:https?:|mailto:|tel:|#|javascript:)})

    path = reference.split(/[?#]/, 2).first
    next if path.nil? || path.empty?

    target = file.dirname.join(path).cleanpath
    missing << "#{file.relative_path_from(root)}: #{reference}" unless target.exist?
  end
end

root.glob("assets/css/*.css").each do |file|
  file.read.scan(/url\(["']?([^\)"']+)/).flatten.each do |reference|
    next if reference.match?(%r{^(?:https?:|data:|#)})

    path = reference.split(/[?#]/, 2).first
    target = file.dirname.join(path).cleanpath
    missing << "#{file.relative_path_from(root)}: #{reference}" unless target.exist?
  end
end

if missing.empty?
  puts "All local HTML and CSS references resolve."
else
  warn "Missing local references:"
  missing.each { |item| warn "- #{item}" }
  exit 1
end
